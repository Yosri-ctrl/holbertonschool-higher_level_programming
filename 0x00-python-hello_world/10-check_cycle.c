#include "lists.h"
/**
*check_cycle - check if the is a cycle or not
*@list: the list to check
*Return: 0 if there is no cycle || 1 if exist
*/
int check_cycle(listint_t *list)
{
	listint_t *current;

	if(list == NULL)
		return(0);
	current = list;
	while(current->next != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
