#include "lists.h"

/**
 * palindromo - Auxiliar variable with recursivity.
 * @head: Head of the linked list.
 * @num: Counter for each cicle, it going decreassing.
 * @len: lenght to rebase if is a palindrome.
 * Return: Always 0.
 */
int palindromo(listint_t *head, int *num, int len)
{
	listint_t *inicio, *current;
	int i;

	inicio = head;
	current = head;
	for (i = 1; i < *num; i++)
	{
		current = current->next;
	}
	if (*num < len)
		return (1);
	else if (inicio->n == current->n)
	{
		*num -= 2;
		return (palindromo(head->next, num, len));
	}
	else
		return (0);
}

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Head of the linked list.
 * Return: 1 if it is, 0 if doesn't.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int lenght = 0, num = 0;

	while (current->next != NULL)
	{
		lenght++;
		current = current->next;
	}

	num = lenght + 1;
	if (num % 2 == 0)
		lenght = 2;
	else
		lenght = (lenght - 1) / 2;
	return (palindromo(*head, &num, lenght));
}
