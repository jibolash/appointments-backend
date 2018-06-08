#!/usr/bin/perl
use strict;

use JSON;
use CGI;
use DBI;

use DatabaseHelper;

my $cgi = new CGI;

my $db = "db.sqlite";

my $databaseHelper = DatabaseHelper->new;

my $driver = "SQLite";
my $dsn = "DBI:$driver:dbname=$db";
my $dbh = DBI->connect($dsn) or die "Cannot cannot to database";


my $sth = $dbh->prepare("CREATE TABLE IF NOT EXISTS appointment(id INTEGER PRIMARY KEY, time TEXT, date TEXT, description TEXT)");
$sth->execute();

if($cgi->param("newFlag")){
    my $date = $cgi->param('date');
    my $time = $cgi->param('time'); 
    my $desc = $cgi->param('description');

    $databaseHelper->createAppointment($dbh, $date, $time, $desc);
}

my @results;

if($cgi->param("searchString")){
    my $desc = $cgi->param("searchString");
    @results = $databaseHelper->getAppointments($dbh, $desc);    
}
else {    
    @results = $databaseHelper->getAppointments($dbh, undef);
}

$dbh->disconnect();
my $json->{"appointments"} = \@results;
my $appointments = encode_json $json;


print $cgi->header(-type=>"application/json", -charset=>"utf-8");
print $appointments;
