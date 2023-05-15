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
	listint_t *sl = *head, *fa = *head, *prev = NULL, *temp;

	while (fa && fa->next)
	{
		fa = fa->next->next;
		temp = sl->next;
		sl->next = prev;
		prev = sl;
		sl = temp;
	}

	if (fa)
		sl = sl->next;

	while (sl)
	{
		if (prev->n != sl->n)
			return (0);

		prev = prev->next;
		sl = sl->next;
	}

	return (1);
}
