#!/usr/bin/perl

use warnings;
use strict;

use constant PI => 4 * atan2(1,1);

sub vol  { my $n = shift; $n == 0 ? 1 : surf($n-1) / $n    }
sub surf { my $n = shift; $n == 0 ? 2 : 2 * PI * vol($n-1) }

my $D = $ARGV[0] || 4;
my $N = $ARGV[1] || 100;

my $expected_volume = vol($D) / 2**$D;

my ($success, $total) = (0,0);

for(1..$N) {
    my $v = 0;
    $v += rand()**2 for 1..$D;

    $success++ if $v <= 1;
    $total++;

    print +($success / $total - $expected_volume) / $expected_volume, $/;
}
