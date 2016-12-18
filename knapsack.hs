{-# LANGUAGE BangPatterns, GeneralizedNewtypeDeriving #-}
module Main where

import Prelude
import Data.List (foldl')
import qualified Data.Vector as V
import Control.Applicative
import Control.Monad.State
import System.Random
import Data.IORef

newtype R a = MkR { draw :: IO a }
    deriving (Functor, Applicative, Monad)

createChain :: a -> (a -> IO a) -> IO (R a)
createChain x0 step = do
    v <- newIORef x0
    return $ MkR $ do
        x  <- readIORef v
        x' <- step x
        writeIORef v x'
        return x'

ex_a :: V.Vector Int
ex_a = V.fromList [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,7,7,7,7,7,7,7,7,9,9,9,9]

admissible :: V.Vector Int -> Int -> V.Vector Bool -> Bool
admissible a b x = V.sum (V.zipWith (\u v -> if u then v else 0) x a) <= b

createSampler :: V.Vector Int -> Int -> IO (R (V.Vector Bool))
createSampler a b = createChain (V.replicate n False) step
    where
    n      = V.length a
    step x = withProbability 0.5 x $ do
        i <- randomRIO (0, n - 1)
        let x' = x V.// [(i, not (x V.! i))]
        return $ if admissible a b x' then x' else x

estimateExpectation :: (Floating a) => Int -> R a -> IO a
estimateExpectation n v = mean <$> replicateM n (draw v)

estimateProportion :: Int -> R a -> (a -> Bool) -> IO Double
estimateProportion n v p = estimateExpectation n $ liftM (\x -> if p x then 1 else 0) v

estimateSize :: V.Vector Int -> Int -> IO ()
estimateSize a b = do
    indicators <- V.forM (V.zip bs (V.tail bs)) $ \(b0,b1) -> do
        c <- createSampler a b1
        replicateM_ 1000 $ draw c
        return $ MkR $ admissible a b0 <$> draw c
    forM_' [(1::Int)..] (V.replicate (V.length a) (0::Int)) $ \n totals -> do
        newValues <- V.forM indicators draw
        let totals' = V.zipWith (\r z -> if z then r + 1 else r) totals newValues
        print $ recip $ V.product $ V.map (\q -> fromIntegral q / fromIntegral n) totals'
        return totals'
    where
    bs = V.map (min b) $ V.scanl' (+) 0 a

exactSize :: V.Vector Int -> Int -> Int
exactSize a b = length $ filter (admissible a b) $ V.replicateM n [False,True]
    where
    n = V.length a

main :: IO ()
main = estimateSize ex_a 40

forM_' :: (Monad m) => [a] -> s -> (a -> s -> m s) -> m ()
forM_' xs s f = go xs s
    where
    go []     _ = return ()
    go (x:xs) s = f x s >>= (\s' -> go xs s')

withProbability :: (MonadIO m) => Double -> a -> m a -> m a
withProbability p x m = do
    q <- liftIO randomIO
    if q >= p then m else return x

-- aus Math.Statistivs
mean :: Floating a => [a] -> a
mean xs = fst $ foldl' (\(!m, !n) x -> (m+(x-m)/(n+1),n+1)) (0,0) xs
