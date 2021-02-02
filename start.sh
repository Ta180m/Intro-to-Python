echo "Which section? (C 1 2 3 T A E)"
read section_number

if [ $section_number == C ]
then
    python -i console.py

elif [ $section_number == T ]
then
	echo "Which file?"
	read file_name
	python -i tictactoe/${file_name}.py

elif [ $section_number == A ]
then
    echo "Which file?"
    read file_name
    python -i advanced/${file_name}.py

elif [ $section_number == E ]
then
    python -i epilogue.py

else
    echo "Which file?"
    read file_name
    python -i section${section_number}/${file_name}.py

fi
