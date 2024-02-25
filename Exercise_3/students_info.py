import lxml.etree as et

xml_file = 'students.xml'

tree = et.parse(xml_file) 
root = tree.getroot()


def student_info(data,element):
    print(f'---{element}---')
    if isinstance(data,str):
        print(data)
    elif isinstance(data,dict):
        for key,value in data.items():
            print(f'{key}:{value}')
    elif isinstance(data,list):
        for item in data:
            print(item)
    print("\n")

student_info(root.find('title').text,'title')
student_info(root.find('description').text,'description')

student_names = []
for student in root.findall('student'):
    info_data = {
        "name": student.find('name').text,
        "age": student.find('age').text,
        "gender": student.find('gender').text,
        "class": student.find('class').text,
        'subjects_info': []
    }
    
    student_names.append(info_data)
    for item in student.findall('subjects/subject'):
        subject_data = {
            "subject_name": item.find('name').text,
            'grade': item.find('grade').text
        }
        info_data['subjects_info'].append(subject_data)
        
student_info(student_names,'names')