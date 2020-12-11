echo "Which section? (1/2/3)"
read section_number
echo "Which file?"
read file_name
python -i section${section_number}/${file_name}.py
