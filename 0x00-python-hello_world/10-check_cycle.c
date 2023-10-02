#include "lists.h"

/**
 * check_cycle - A function that checks if there's a cycle in a list
 *
 * @list: The linked list to test on.
 *
 * Return: 0 if there's no loop.
 *         1 if there is.
*/
int check_cycle(listint_t *list)
{
	listint_t *head = list, *temp = list;

	while (head && temp)
	{
		head = head->next;

		if (temp->next || temp->next->next)
			temp = temp->next->next;
		else
			break;

		if (head == temp)
			return (1);
	}

	return (0);
}
