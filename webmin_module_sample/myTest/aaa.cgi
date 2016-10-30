#!/usr/bin/perl

require './myTest-lib.pl';
ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

print "<!DOCTYPE html>\n";
print "<html>\n";
print "<head>\n";
print "<title>Page Title</title>\n";
print "</head>\n";
print "<body>\n";

#read input cgi parameters
&ReadParse();
foreach $key (keys %in) {
    print "<p>key= $key, value = $in{$key}</p>\n";
};


print "</body>\n";
print "</html>\n";

ui_print_footer("/", $text{'index'});
