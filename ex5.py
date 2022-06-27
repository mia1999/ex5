import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    with open(input_json_path, 'r') as file:
        students_db_dict = json.load(file)
    
    list_of_names = []
    
    for info_dict in students_db_dict.values():
        for course in info_dict['registered_courses']:
            if course == course_name:
                list_of_names.append(info_dict['student_name'])
    
    return list_of_names


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path, 'r') as input_file:
        students_db_dict = json.load(input_file)
    
    list_of_courses = []

    for info_dict in students_db_dict.values():
        for course in info_dict['registered_courses']:
            list_of_courses.append(course)
    
    list_of_courses.sort()
    dict_of_enroll_nums = {}
    for course in list_of_courses:
        dict_of_enroll_nums[course] = 0
    for course in list_of_courses:
        dict_of_enroll_nums[course] += 1
    
    with open(output_file_path, 'w') as output_file:
        for course, enroll_num in dict_of_enroll_nums.items():
            output_file.write('"' + course + '" ' + str(enroll_num) + "\n")


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    for file in os.listdir(json_directory_path):
        file_path = os.path.join(json_directory_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as input_file:
                semester_db_dict = json.load(input_file)

    courses_for_lecturers_dict = {}

    for course_info in semester_db_dict.values():
        for lecturer in course_info["lecturers"]:
            courses_for_lecturers_dict[lecturer] = [].append(course_info["course_name"])
    
    with open(output_json_path, 'w') as output_file:
        json.dump(courses_for_lecturers_dict, output_file)