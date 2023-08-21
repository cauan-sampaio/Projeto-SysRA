Feature: ADM cursos

        Scenario: O usuário irá logar na conta e criar um curso
            Given O usuário entra na página de login
            When O usuário digitar os seus dados de login
            """
            {
            "matricula": "20221045050443",
            "senha":"87489308Ca#"
            } 
            """ 
            Then O usuário entrará na página inicial e irá clicar em ADM, e depois em cursos
        
        Scenario:Cria curso
            Given O usuário entra na página de cursos
            When O usuário clicar no botão para criar um novo curso

            """
            {
            "curso": "Técnico em ADM"
            }
            """ 
            Then O usuário criou o novo curso