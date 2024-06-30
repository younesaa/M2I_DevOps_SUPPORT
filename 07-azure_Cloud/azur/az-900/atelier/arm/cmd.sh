for resource_id in $(az resource list --resource-group wkl --query "[].name" -o tsv);
do az resource delete --name $resource_id --resource-group wkl; 
done
