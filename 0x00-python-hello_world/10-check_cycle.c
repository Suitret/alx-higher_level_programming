#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_nodecp - adds a new node
 * @head: pointer to a pointer of the start of the list
 * @adr: adress to be included in node
 * Return: address of the new element or NULL if it fails
 */
cplist *add_nodecp(cplist **head, listint_t *adr)
{
	cplist *new;

	new = malloc(sizeof(cplist));
	if (new == NULL)
		return (NULL);

	new->adr = adr;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listcp - frees a listcp list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listcp(cplist *head)
{
	cplist *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * check_cycle - cheks if there is a cycle
 * @list: given list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	cplist *head = NULL, *temp, *cur;
	listint_t *ptr;
	int flag = 0;

	while (list)
	{
		temp = add_nodecp(&head, list);
		ptr = list;
		list = list->next;
		ptr->next = NULL;
	}
	cur = head->next;
	while (cur)
	{
		if (cur->adr == temp->adr)
		{
			flag = 1;
			break;
		}
		cur = cur->next;
	}
	cur = (flag == 1) ? (head->next) : (head);
	while (cur)
	{
		temp = cur->next;
		if (temp)
			temp->adr->next = cur->adr;
		else
			break;
		cur = cur->next;
	}
	if (flag)
		head->next->adr->next = head->adr;

	free_listcp(head);
	return (flag);
}
