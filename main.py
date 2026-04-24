from entidades.atletica import Atletica
from entidades.gestor_geral import GestorGeral
from datetime import date

atletica1 = Atletica("A5")
atletica2 = Atletica("ATM")

gestor = GestorGeral("Kayo", "kayo@gmail.com", "senha", 48999999999)

print(atletica1.nome, "- penalidades:", atletica1.penalidades)
print(atletica2.nome, "- penalidades:", atletica2.penalidades)

gestor.analisar_denuncia(atletica1, atletica2, date.today(), "ATM não compareceu com os atletas no Vôlei Feminino")

print(atletica1.nome, atletica1.penalidades)
print(atletica2.nome, atletica2.penalidades)