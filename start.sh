echo "Which section? (1/2/3/C)"
read section_number
if [ $section_number == C ]; then
    python -i console.py
else
    echo "Which file?"
    read file_name
    python -i section${section_number}/${file_name}.py
fi
