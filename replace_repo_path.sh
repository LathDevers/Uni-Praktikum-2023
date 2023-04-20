#!/bin/bash

echo "Enter path to folder containing .md files (leave empty for using the directory where this script is located):"
read folder_path

if [ -z "$folder_path" ]; then
    folder_path=$(dirname "$(realpath "$0")")
fi

echo "Enter the text to replace:"
read find_text

echo "Enter the new text:"
read replace_text

for file in "$folder_path"/*.md
do
    if [ -f "$file" ]; then
        if grep -q "$find_text" "$file"; then
            sed -i "" "s|$find_text|$replace_text|g" "$file"
            echo "$(basename "$file") | EDITED"
        else
            echo "$(basename "$file") | not changed"
        fi
    fi
done

if [ -z "$(ls $folder_path/*.md 2>/dev/null)" ]; then
    echo "No markdown files found!"
else
    echo "Done!"
fi

#https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app/raw/main/docs/wiki-src/
#https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/flutter-training/raw/master/src/

#https://github.com/LathDevers/flutter-training/blob/master/src/