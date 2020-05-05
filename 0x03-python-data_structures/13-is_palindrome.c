#include "lists.h"
/**
*is_palindrome - check if a list is a palindrom
*@head: the list to check
*Return: If palindron return 0
*/
int is_palindrome(listint_t **head)
{
    listint_t *node, *first, *second;

    node = *head;
    if (node->next == NULL)
        return (1);
    second = *head;
    first = second->next;
    while (first->next)
        first = first->next;

    while (node->next)
    {
        second = *head;
        while (second->next != first)
            second = second->next;
        if (node->n != first->n)
            return (0);
        first = second;
        node = node->next;
    }
    return (1);
}
