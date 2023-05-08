#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct cplist - singly linked list
 * @adr: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct cplist
{
	listint_t *adr;
	struct cplist *next;
} cplist;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

cplist *add_nodecp(cplist **head, listint_t *adr);
void free_cplist(cplist *head);

#endif /* LISTS_H */
