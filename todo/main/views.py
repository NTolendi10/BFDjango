from django.shortcuts import render


tasks =[{'name': 'Task 0',
         'created': '10/09/2018',
         'due_on': '12/09/2018',
         'owner': 'admin',
         'completed': True
         },
        {'name': 'Task 1',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'completed': False
    },
        {'name': 'Task 2',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'completed': False
    },
        {'name': 'Task 3',
         'created': '10/09/2018',
         'due_on': '12/09/2018',
         'owner': 'admin',
         'completed': False
         },
        {'name': 'Task 4',
         'created': '10/09/2018',
         'due_on': '12/09/2018',
         'owner': 'admin',
         'completed': False
         },
    ]


def todo(request):
    task = [i for i in tasks if not i["completed"]]
    context = {"tasks": task, "completed": False}
    return render(request, 'todo_list.html', context=context)



def completed(request):
    task = [i for i in tasks if i["completed"]]
    context = {"tasks": task, "completed": True}
    return render(request, 'completed_todo_list.html', context=context)