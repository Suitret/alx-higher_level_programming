#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * search - searches a node in list
 * @list: given list
 * @node: given node
 * Return: 0 or 1
 */
int search(listint_t *list, listint_t *node)
{
	while (list)
	{
		if (list == node)
			return (1);
		list = list->next;
	}
	return (0);
}

/**
 * check_cycle - cheks if there is a cycle
 * @list: given list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head = NULL, *temp, *tmp;

	if (!list)
		return (0);

	head = list;
	list = list->next;
	head->next = NULL;

	while (list)
	{
		if (search(head, list))
			break;
		temp = list;
		list = list->next;
		temp->next = head;
		head = temp;
	}

	temp = head;
	head = head->next;
	temp->next = list;

	while (head)
	{
		tmp = head;
		head = head->next;
		tmp->next = temp;
		temp = tmp;
	}
	if (list)
		return (1);
	else
		return (0);
}
