#!/user/bin/perl

package DatabaseHelper;

use strict;

sub new {
    my $self = bless { };
    return $self;
}  

sub createAppointment {
    my ($self, $dbh, $date, $time, $description) = @_;
    my $sth = $dbh->prepare("INSERT INTO appointment (`time`, `date`, `description`) VALUES (?, ?, ?)");

    $sth->bind_param(1, $time);
    $sth->bind_param(2, $date);
    $sth->bind_param(3, $description);

    $sth->execute() or die "Could not insert into database";
}

sub getAppointments {
    my ($self, $dbh, $description, $all) = @_;
    my $sth;
    my @results;    

    if(! defined $description){
	    $sth = $dbh->prepare("SELECT `id` AS id, `time` AS time, `date` AS date, `description` AS description FROM appointment");	
    }
    else {
	    $sth = $dbh->prepare("SELECT `id` AS id, `time` AS time, `date` AS date, `description` AS description FROM appointment WHERE description LIKE '%$description%'");	
    }    

    $sth->execute() or die "Could not execute prepared statement";
    
    while (my $row = $sth->fetchrow_hashref) {
	    push @results, $row;
    }
    return @results;
}

1
