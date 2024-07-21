import flet as ft

from models import Produto


def main(page: ft.Page):
    page.title = "Cadastro App"
    session = Produto.create_session()
    lista_produtos = ft.ListView()

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                )
            )
            txt_erro.visible = False
            txt_acerto.visible = True
        except:
            txt_erro.visible = True
            txt_acerto.visible = False
        page.update()

    txt_erro = ft.Container(ft.Text('Erro ao salvar!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Salvo com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)

    text_titulo = ft.Text('Titulo do produto:')
    produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_erro,
        txt_acerto,
        text_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

    page.add(
        lista_produtos
    )

if __name__ == "__main__":
    ft.app(target=main)
