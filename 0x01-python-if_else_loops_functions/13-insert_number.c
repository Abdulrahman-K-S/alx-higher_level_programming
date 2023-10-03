#include "lists.h"

/**
 * insert_node - A function that inserts a node in a sorted linked list.
 *
 * @head: The head of the linked list.
 * @number: The number to insert.
 *
 * Return: The updated linked list.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	while (temp)
	{
		if (number > temp->n && number < temp->next->n)
		{
			node->next = temp->next;
			temp->next = node;
		}

		temp = temp->next;
	}

	return (temp);
}
