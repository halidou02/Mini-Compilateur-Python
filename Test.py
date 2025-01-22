import os
import subprocess
import glob


def Evaluate_student(ResultsInter, verbose =False,ShowError=False):
     
     path = 'StudentCode'
     for Student  in os.listdir(path):
                    # Calculate notelex and noteyac
                    false_lex_accepted = 0 # Update with actual value
                    false_lex_not_accepted = 0 # Update with actual value
                    false_yac_accepted = 0 # Update with actual value
                    false_yac_not_accepted = 0 # Update with actual value

                    # Get interpreter results
                    interpreter_results = 0 # Update with actual value
                    print(f"-->{Student}") 
                    if verbose:   
                         print('\t Test Lexical')
                         print('\t \t Run accepted ')
                    for prog in os.listdir('Accepted_all'):
                         if prog.endswith('.txt') :
                              
                              # define the command to be executed
                              command = ['python', f'StudentCode/{Student}/lex.py', f'Accepted_all/{prog}']

                              # run the command as a subprocess
                              process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                              # read the output and error messages from the subprocess
                              output, error = process.communicate()

                              # print the output and error messages
                              
                              if len(output)>0 and 'Not' not in str(output.decode('utf-8')):
                                        if verbose:
                                             print(f'\t\t\t\tThe {prog} should be accepted ')
                                        false_lex_accepted+=1
                              else :
                                   print(f'\t\t\t\tThe lex_Accepted_all/{prog} should be accepted ')
                              if ShowError:
                                   print("Accepted_all - Lexical Errors prog:",prog)
                                   print(error)
                    if verbose:
                         print('\t \t Run not accepted')
                    for prog in os.listdir('Not_accepted_lex'):
                         if prog.endswith('.txt') :

                              command = ['python', f'StudentCode/{Student}/lex.py', f'Not_accepted_lex/{prog}']

                              # run the command as a subprocess
                              process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                              # read the output and error messages from the subprocess
                              output, error = process.communicate()

                              # print the output and error messages
                              
                              if len(output)>0 and 'Not' in str(output.decode('utf-8')):
                                   false_lex_not_accepted+=1
                                   if verbose:
                                        print(f'\t\t\t\tThe {prog} should not be accepted ')
                              else:
                                   print(f'\t\t\t\tThe lex_Not_accepted_lex/{prog} should not be accepted ')
                              if ShowError:
                                   print("Not Accepted All- Lexical Errors prog:",prog)
                                   print(error)
                    if verbose:
                         print('\t Test Syntax')
                         print('\t \t Run accepted ')
                    for prog in os.listdir('Accepted_all'):
                         if prog.endswith('.txt') :
                              
                              # define the command to be executed
                              command = ['python', f'StudentCode/{Student}/parse.py', f'Accepted_all/{prog}']
                              # run the command as a subprocess
                              process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                              # read the output and error messages from the subprocess
                              output, error = process.communicate()
                              # print the output and error messages
                         
                              if len(output)>0 and 'Not' not in str(output.decode('utf-8')):
                                        if verbose:
                                             print(f'\t\t\t\tThe {prog} should be accepted ')
                                        false_yac_accepted+=1
                              else : 
                                   print(f"\t\t\t\tThe parse Accepted_all/{prog} should be accepted ")
                                   
                              if ShowError:
                                   print(" Accepted All- syntaxe Errors prog:",prog)
                                   print(error)
                    if verbose:
                         print('\t \t Run Not accepted ')
                    for prog in os.listdir('Not_accepted_syntax'):
                         if prog.endswith('.txt') :
                              
                              command = ['python', f'StudentCode/{Student}/parse.py', f'Not_accepted_syntax/{prog}']

                              # run the command as a subprocess
                              process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                              # read the output and error messages from the subprocess
                              output, error = process.communicate()

                              # print the output and error messages
                              
                              if len(output)>0 and 'Not' in str(output.decode('utf-8')):
                                        false_yac_not_accepted+=1
                                        if verbose:
                                             print(f'\t\t\t\tThe {prog} should not be accepted ')
                              else :
                                   print(f'\t\t\t\tThe parse Not_accepted_syntax/{prog} should not be accepted ')
                              if ShowError:
                                   print(" Not Accepted All- syntaxe Errors prog:",prog)
                                   print(error)
                    if verbose:
                         print('\t Generate Symentique ABR')
                    for prog in os.listdir('Accepted_ABR'):
                         if prog.endswith('.txt') :
                              command = ['python', f'StudentCode/{Student}/threader.py', f'Accepted_ABR/{prog}',Student]

                              # run the command as a subprocess
                              process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                              # read the output and error messages from the subprocess
                              output, error = process.communicate()

                              if ShowError:
                                   print(" ABR Creation Errors prog:",prog)
                                   print(error)
                              
                         
                    if verbose:
                         print('\t Test interpreter')
                    for prog in os.listdir('Accepted_Inter'):
                         if prog.endswith('.txt') :
                              command = ['python', f'StudentCode/{Student}/Interpreter.py', f'Accepted_Inter/{prog}']

                              # run the command as a subprocess
                              process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                              # read the output and error messages from the subprocess
                              output, error = process.communicate()
                              
                              if len(output)>0 and  ResultsInter[prog]==int(output.decode('utf-8')):
                                   interpreter_results+=1
                              else:
                                   if verbose:
                                        print(f"The results should be {ResultsInter[prog]} and {int(output.decode('utf-8'))} was outputed ")
                              if ShowError:
                                   print(" Interpretore Errors prog:",prog)
                                   print(error)                 

                    # Define file paths
                    accepted_folder_path = "Accepted_all/"
                    not_accepted_lex_folder_path = "Not_accepted_lex/"
                    not_accepted_syntax_folder_path = "Not_accepted_syntax/"
                    accepted_inter_folder_path = "Accepted_Inter/"

                    # Get file counts
                    total_accepted_count = len(glob.glob(accepted_folder_path + "*.txt"))
                    not_accepted_lex_count = len(glob.glob(not_accepted_lex_folder_path + "*.txt"))
                    not_accepted_syntax_count = len(glob.glob(not_accepted_syntax_folder_path + "*.txt"))
                    accepted_inter_count = len(glob.glob(accepted_inter_folder_path + "*.txt"))

                  
                   
                    note_lex = ( false_lex_accepted + false_lex_not_accepted) 
                    note_yac = ( false_yac_accepted + false_yac_not_accepted)
                    
                    

                    # Calculate final note
                    note_final = (note_lex + note_yac + interpreter_results) / 3

                    # Print results
                    print("Note lex:", note_lex, "/", total_accepted_count + not_accepted_lex_count)
                    print("Note syntax:", note_yac, "/", total_accepted_count + not_accepted_syntax_count)
                    print("Note interpreteur:", interpreter_results, "/", accepted_inter_count)
                    print("Note finale:", note_final)
verbose =False
ResultsInter={'prog0.txt':1,
              'prog1.txt':10,
              'prog2.txt':5,
              'prog3.txt':1,
              'prog4.txt':5,
              'prog5.txt':35,
              'prog6.txt':7,
}
Evaluate_student(ResultsInter, verbose =False,ShowError=False)

input()
    