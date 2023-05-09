#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node in list
 * @head: pointer to the start of the list
 * @number: value
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *pnext;

	if (!head)
		return (NULL);

	current = *head;
	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		pnext = current->next;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
			pnext = current->next;
		}
		current->next = new;
		new->next = pnext;
	}

	return (new);
}
