echo "Which section? (1/2/3/C/T)"
read section_number

if [ $section_number == C ]
then
    python -i console.py

elif [ $section_number == T ]
then
	echo "Which file?"
	read file_name
	python -i tictactoe/${file_name}.py

else
    echo "Which file?"
    read file_name
    python -i section${section_number}/${file_name}.py

fi
