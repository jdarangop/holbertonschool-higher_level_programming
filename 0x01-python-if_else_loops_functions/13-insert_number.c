#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Insert a new node in a sorted list.
 * @head: list
 * @number: number
 * Return: Always 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (head == NULL)
	{ *head = new_node;
		return (*head);
	}
	if (current->next == NULL)
	{
		if (current->n < number)
		{
			current->next = new_node;
			new_node->next = NULL;
			return (new_node);
		}
		else
		{
			new_node->next = current;
			*head = new_node;
			return (*head);
		}
	}
	while (current->next != NULL)
	{
		if (current->n < number && current->next->n > number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		else
			current = current->next;
	}
	current->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
