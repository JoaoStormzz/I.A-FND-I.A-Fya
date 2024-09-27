<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IA</title>
</head>
<body>
    <form method="post">
        <input type="text" name="user_input" placeholder="" required>
        <button type="submit">Enviar</button>
    </form>

    <?php 
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $userInput = escapeshellarg($_POST['user_input']); // Escapando a entrada do usuário
            $cmdExecPy = shell_exec("python main.py $userInput");
            echo "<p>Resposta: $cmdExecPy</p>";
        }
    ?>
</body>
</html>