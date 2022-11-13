from handlers import HandlerRegister
from handlers.document import DocumentHandler
from handlers.job import JobHandler
from handlers.user import UserHandler
from search import search

register = HandlerRegister()
users = UserHandler(['christ','idourah','yoane','bahamboula','jessica','joana','kinya'])
jobs = JobHandler(['C++','Java','JavaScript','C#','C', 'PHP'])
documents = DocumentHandler(['pdf','word','excel','presentation'])

register.append(users)
register.append(jobs)
register.append(documents)

head = register.head

response = search(head, {'q':'word'})

print(response)
