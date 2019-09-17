#include "lists.h"


/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Head of the linked list.
 * Return: 1 if it is, 0 if doesn't.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *inicio, *final;
	int lenght = 0, count = 0, i = 0, j;

	while (current->next != NULL)
	{
		lenght++;
		current = current->next;
	}
	count = lenght + 1;
	while (i != count / 2)
	{
		inicio = *head;
		final = *head;

		for (j = 0; j < i; j++)
		{
			inicio = inicio->next;
		}
		for (j = 0; j < count - (i + 1); j++)
		{
			final = final->next;
		}
		if (inicio->n != final->n)
		{
			return (0);
		}
		else
		{
			i++;
		}
	}
	return (1);
}
