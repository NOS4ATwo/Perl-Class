#!C:\Perl\bin\perl
use strict;
print "Hello World \n";
print "----Begin----\n";
#	Create array
my @array;
print "##File Read##\n";
#	Read in 10 Values from file
my $filename='pstalnaker_PPS_lab2_data1.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $row = <$fh>) {
  chomp $row;
  print "$row\n";
  push(@array, $row);
}
print "done\n";
print "##Array read##\n";
#check it works
print "$_\n" for @array;
#Sort the Array
@array = sort(@array);
print "##after array sort##\n";
print "$_\n" for @array;

#Print the size out of the Array to the screen
my $size = @array;
print "##########Size:  $size#####\n";
#Print the Array to the screen
print "$_\n" for @array;
#Delete the values in the array
@array=();
my $size = @array;
#Print the array size
print "$_\n" for @array;
print "##########Size:  $size######\n";