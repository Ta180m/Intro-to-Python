echo "Which lesson? (1/2/3)"
read lesson_number
echo "Which file?"
read file_name
python -i lesson${lesson_number}/${file_name}.py
