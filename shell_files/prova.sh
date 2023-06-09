results_folder_path=$(pwd)/../results/

for item in $results_folder_path*; do
    # Extract the name of the item
    name=$(basename "$item")
	echo $name

done

