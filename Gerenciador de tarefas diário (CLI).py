tarefas = []
voltar_menu=("\nPressione qualquer tecla para voltar ao menu")

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Consultar tarefas")
    print("3 - Marcar tarefa como concluida")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")


#adicionar tarefa
    if opcao=="1":
        nova_tarefa=input("Digite a nova tarefa:")
        inicio_tarefa=input("Digite a hora inicial da tarefa(ex:18:00):")
        fim_tarefa=input("Digite a hora final para conclusão da tarefa(ex:19:30):")

        tarefa=[nova_tarefa,inicio_tarefa,fim_tarefa,"Pendente"]
        
        #adiciona a nova tarefa junto com as outras
        tarefas.append(tarefa)
        
        print("Tarefa adicionada com sucesso!")
        input(voltar_menu)


#consultar as tarefas
    elif opcao=="2":
        if len(tarefas)==0:
            print("Nenhuma tarefa cadastrada.")
            input(voltar_menu)
            
        
        else:
            print("\n     ROTINA DO DIA     ")
       #numera as tarefas começando do 1
            for i, tarefa in enumerate(tarefas,start=1):
         
         
                print(f"{i} - {tarefa[0]} | {tarefa[1]}-{tarefa[2]} | {tarefa[3]}")

            input(voltar_menu)


#concluir tarefa
    elif opcao=="3":
        if len(tarefas)==0:
             print("Não a tarefas para excluir.")
             input(voltar_menu)
            

        for i, tarefa in enumerate(tarefas,start=1):
            print(f"{i} - {tarefa[0]} | {tarefa[1]}-{tarefa[2]} | {tarefa[3]}")

        concluir_tarefa=int(input("Digite o numero da tabela que vc quer concluir?"))
        if 1<=concluir_tarefa<=len(tarefas):
            
            #altera o Pendente para Concluida
            tarefas[concluir_tarefa-1][3] = "Concluída"
                
            print("Parabens! Uma nova tarefa foi concluída com sucesso!")
        else:
            print("Número inválido!")
            input(voltar_menu)


#exluir tarefa
    elif opcao=="4":
        if len(tarefas)==0:
             print("Não a tarefas para excluir.")
             input(voltar_menu)
             continue
        
        for i, tarefa in enumerate(tarefas,start=1):
            print(f"{i} - {tarefa[0]} | {tarefa[1]}-{tarefa[2]} | {tarefa[3]}")

        excluir_tarefa=int(input("Digite o numero da tabela que vc quer excluir?"))
        if 1<=excluir_tarefa<=len(tarefas):
            tarefas.pop(excluir_tarefa-1)
            print("Tarefa removida com sucesso!")
        
        else:
            print("Número inválido!")
            input(voltar_menu)


    elif opcao=="5":
        print("Saindo do sistema...")
        break


    else:
        print("Opção inválida!")
        input(voltar_menu)