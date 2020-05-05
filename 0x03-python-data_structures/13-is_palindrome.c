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
    if (node->next == NULL)
        return (1);
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
    second = new;
    while (node->next)
    {
        if (node->n != second->n)
        {
            free_listint(new);
            return (0);
        }
        node = node->next;
        second = second->next;
    }
    free_listint(new);
    return (1);
}
