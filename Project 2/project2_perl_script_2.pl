#!C:\Perl\bin\perl
use strict;
print "Hello World \n";
print "----Begin----\n";
print "----Begin_First_Array----\n";

#2.  Create a perl script that will do the following       

#       a.  create two different arrays
my @key;
my @keyvalue;
my @value;
my $size;
my %hash;
#	Read in 10 Values from file
my $filename='pstalnaker_PPS_lab2_data2.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $row = <$fh>) {
  chomp $row;
  print "$row\n";
  push(@key, $row);
}
print "done\n";
print "##Array read##\n";
#check it works
print "$_\n" for @key;
print "----Begin_Second_Array----\n";
#	Read in 10 Values from file
my $filename='pstalnaker_PPS_lab2_data3.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $row = <$fh>) {
  chomp $row;
  print "$row\n";
  push(@value, $row);
}
print "done\n";
print "##Array read##\n";
#check it works
print "$_\n" for @value;
print "----Starting_Hash_Stuff----\n";
#	b. combine two arrays into hash
@hash{@key} = @value;
#       b.  Print out the key/value pairs.       
print %hash;
print "\n";
print map { "$_ => $hash{$_}\n" } keys %hash;
#       c.  Print the size of the hash.       
$size = keys %hash;
print "hash size: is $size\n";
#       d.  delete all the key/value pairs.       
undef %{hash};
#       e.  Print the size of the hash. 
$size = keys %hash;
print "hash size: is $size\n";