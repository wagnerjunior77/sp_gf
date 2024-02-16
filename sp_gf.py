import customtkinter
from datetime import datetime, timedelta
customtkinter.set_appearance_mode("System")  # Novo: Define o modo de aparência
customtkinter.set_default_color_theme("blue")  # Selecione um dos temas pré-definidos

def modify_time(time_str, variable, operation):
    # Valores das variáveis 2, 3 e 4 em segundos
    variables = {2: 7.358, 3: 11.529, 4: 15.536}
    
    # Convertendo a minutagem fornecida para um objeto datetime
    try:
        initial_time = datetime.strptime(time_str, '%M:%S.%f')
    except ValueError:
        return "Formato de tempo inválido. Use minuto:segundo.milissegundo"
    
    # Selecionando o valor da variável
    duration = variables.get(variable, 0)
    
    # Calculando o novo tempo baseado na operação escolhida
    if operation == 1:  # Somar
        modified_time = initial_time + timedelta(seconds=duration)
    elif operation == 2:  # Subtrair
        modified_time = initial_time - timedelta(seconds=duration)
    else:
        return "Operação inválida. Escolha 1 para somar ou 2 para subtrair."
    
    # Formatando o tempo modificado para o formato de minutos, segundos e milissegundos
    modified_time_str = modified_time.strftime('%M:%S.%f')[:-3]
    return modified_time_str

def calculate():
    time_str = time_entry.get()
    variable = int(variable_entry.get())
    operation = int(operation_var.get())
    
    modified_time = modify_time(time_str, variable, operation)
    result_label.configure(text=f"Tempo modificado: {modified_time}")

app = customtkinter.CTk()
app.title("Modificador de Tempo")

time_label = customtkinter.CTkLabel(app, text="Tempo (minuto:segundo.milissegundo):")
time_label.grid(row=0, column=0, sticky="w")

time_entry = customtkinter.CTkEntry(app)
time_entry.grid(row=0, column=1, sticky="ew")

variable_label = customtkinter.CTkLabel(app, text="SP (2,3,4):")
variable_label.grid(row=1, column=0, sticky="w")

variable_entry = customtkinter.CTkEntry(app)
variable_entry.grid(row=1, column=1, sticky="ew")

operation_label = customtkinter.CTkLabel(app, text="Operação (1-Somar / 2-Subtrair):")
operation_label.grid(row=2, column=0, sticky="w")

operation_var = customtkinter.CTkOptionMenu(app, values=["1", "2"])
operation_var.grid(row=2, column=1, sticky="ew")

calculate_button = customtkinter.CTkButton(app, text="Calcular", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = customtkinter.CTkLabel(app, text="Resultado aparecerá aqui")
result_label.grid(row=4, column=0, columnspan=2, sticky="ew")

app.grid_columnconfigure(1, weight=1)  # Faz com que a coluna 1 expanda para preencher o espaço extra

app.mainloop()