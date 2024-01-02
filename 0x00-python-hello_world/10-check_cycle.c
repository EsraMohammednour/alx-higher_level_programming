#include "lists.h"
/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: pointer
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *esra, *hind;
	if (!list ||!list->next)
		return(0);
	esra = list->next;
	hind = list->next->next;
	while(esra && hind && hind->next)
	{
		if(esra == hind)
			return (1);
		esra = esra->next;
		hind = hind->next->next;
	}
	return (0);
}
