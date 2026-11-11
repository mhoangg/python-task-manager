#!/usr/bin/env bash
set -euo pipefail

tasks_file="$1"
tests_file="$2"
html_file="index.html"

todo_tasks=$(awk '/^ToDo Tasks:$/ {section=1; next} /^Done Tasks:$/ {section=0} section' "$tasks_file")

done_tasks=$(awk '/^Done Tasks:$/ {section=1; next} section' "$tasks_file")

test_results=$(cat "$tests_file")

update_pre() {
    local id="$1" content="$2"

    PRE_ID="$id" PRE_CONTENT="$content" perl -0777 -i -pe '
        BEGIN {
            $id = $ENV{PRE_ID};
            $content = $ENV{PRE_CONTENT};
            $content =~ s/&/&amp;/g;
            $content =~ s/</&lt;/g;
            $content =~ s/>/&gt;/g;
        }
        s{(<pre id="\Q$id\E">).*?(</pre>)}{$1$content$2}sg;
    ' "$html_file"
}

update_pre todo "$todo_tasks"
update_pre done "$done_tasks"
update_pre tests "$test_results"

echo "Updated index.html"
