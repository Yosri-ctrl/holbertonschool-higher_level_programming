#include "lists.h"
/**
*is_palindrome - check if a list is a palindrom
*@head: the list to check
*Return: If palindron return 0
*/
int is_palindrome(listint_t **head)
{
    listint_t *node, *new, *first, *second;

    node = *head;
    new = NULL;
    second = *head;
    first = second->next;

    while (first->next)
    {
        first = first->next;
        second = second->next;
    }

    while (second != node)
    {
        add_nodeint_end(&new, first->n);
        /*print_listint(new);*/
        first = second;
        second = *head;
        while (second->next != first && second)
            second = second->next;
        /*print_listint(new);*/
    }
    add_nodeint_end(&new, first->n);
    add_nodeint_end(&new, second->n);

    while (node->next)
    {
        if (node->n == second->n)
        {
            node = node->next;
            second = second->next;
        }
        else
        {
            free_listint(new);
            return (0);
        }
    }
    free_listint(new);
    return (1);
}
