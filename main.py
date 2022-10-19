import get_data
import file_writing
import print

#my_ph = get_data.data_entry()

#file_writing.writing_scv( 'phonebook.scv', my_ph)
#file_writing.writing_txt('phonebook.txt',my_ph)
print.print_data('phonebook.scv')
print.print_data('phonebook.txt')
file_writing.record_all('All data.csv','phonebook.scv','phonebook.txt')
