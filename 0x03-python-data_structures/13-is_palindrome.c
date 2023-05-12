#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptrn;
	int l = 0, n, flag;

	if (head == NULL)
		return (0);
	printf("ENter\n");
	if (*head == NULL)
		return (1);
	printf("ENter\n");

	ptr = *head;
	while (ptr)
	{
		l++;
		ptr = ptr->next;
	}
	n = (l % 2 == 0) ? (l / 2) : ((l - 1) / 2);
	flag = (l % 2 == 0) ? 1 : 0;

	ptr = *head;
	while (n - 1)
	{
		ptr = ptr->next;
		n--;
	}
	ptrn = (flag) ? (ptr->next) : (ptr->next->next);

	while (ptrn)
	{
		if (ptr->n != ptrn->n)
			return (0);
		ptr = previous(*head, ptr);
		ptrn = ptrn->next;
	}
	return (1);
}

/**
 * previous - searches the precedent of a node
 * @head: pointer to head of list
 * @node: reference node
 * Return: adress of the precedent
 */
listint_t *previous(listint_t *head, listint_t *node)
{
	while (1)
	{
		if (head == node)
			return (node);
		else if (head->next->next == node)
			return (head->next);
		else if (head->next->next == node->next)
			return (head);
		head = head->next->next;
	}
}
