import flet as ft
from models import Produto

def main(page: ft.Page):
    # Definindo o tamanho da janela para simular uma tela de celular
    page.window_width = 375
    page.window_height = 667
    page.title = "Lista de compras"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    session = Produto.create_session()
    lista_produtos = ft.ListView(expand=True, spacing=10)

    def add_new_product(e):
        # Adiciona um novo produto ao banco de dados e atualiza a lista de produtos na interface.
        try:
            novo_produto = Produto(titulo=produto.value, quantidade=float(quantidade.value))
            session.add(novo_produto)
            session.commit()
            add_list_product(novo_produto)
            txt_erro.visible = False
            txt_acerto.visible = True
        except Exception as ex:
            txt_erro.visible = True
            txt_acerto.visible = False
            print(f"Error: {ex}")
        page.update()

    def add_list_product(produto):
        # Adiciona um produto à lista de produtos na interface.
        lista_produtos.controls.append(
            ft.Container(
                ft.Row(
                    [
                        ft.Text(produto.titulo, expand=True),
                        ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, p=produto: update_product(e, p)),
                        ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, p=produto: delet_product(e, p)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor=ft.colors.BLACK12,
                padding=10,
                border_radius=5,
                margin=ft.Margin(0, 0, 0, 10)  # Adicionando margem inferior para espaçamento
            )
        )
        page.update()

    def update_product(e, produto):
        # Abre um diálogo para editar um produto existente.
        novo_titulo = ft.TextField(label="Produto", value=produto.titulo, expand=True)
        novo_quantidade = ft.TextField(label="Quantidade", value=str(produto.quantidade), expand=True)

        def salvar_edicao(ev):
            # Salva as alterações feitas no produto e atualiza a lista de produtos na interface.
            produto.titulo = novo_titulo.value
            produto.quantidade = float(novo_quantidade.value)
            session.commit()
            update_list_product()
            dialog.open = False
            page.update()

        def cancelar_edicao(ev):
            # Fecha o diálogo sem salvar alterações.
            dialog.open = False
            page.update()      

        dialog = ft.AlertDialog(
            title=ft.Text("EDIÇÃO", text_align=ft.TextAlign.CENTER),
            content=ft.Column(
                [
                    novo_titulo,
                    novo_quantidade
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5  # Definindo espaçamento menor entre os campos
            ),
            actions=[
                ft.Row(
                    [
                        ft.TextButton("Salvar", on_click=salvar_edicao),
                        ft.TextButton("Cancelar", on_click=cancelar_edicao),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def delet_product(e, produto):
        # Deleta um produto do banco de dados e atualiza a lista de produtos na interface.
        session.delete(produto)
        session.commit()
        update_list_product()

    def update_list_product():
        # Atualiza a lista de produtos na interface a partir do banco de dados.
        lista_produtos.controls.clear()
        for p in session.query(Produto).all():
            add_list_product(p)
        page.update()

    txt_erro = ft.Container(ft.Text('Erro ao salvar!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Salvo com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)

    text_titulo = ft.Text('Titulo do produto:')
    produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT, expand=True)
    txt_quantidade = ft.Text('Quantidade')
    quantidade = ft.TextField(value="0", label="Digite a quantidade do produto", text_align=ft.TextAlign.LEFT, expand=True)
    btn_produto = ft.ElevatedButton('CADASTRAR', on_click=add_new_product)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    txt_erro,
                    txt_acerto,
                    ft.Row(
                        [text_titulo],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        [produto],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        [txt_quantidade],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        [quantidade],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        [btn_produto],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    lista_produtos
                ],
                expand=True,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=10
        )
    )

    update_list_product()

if __name__ == "__main__":
    ft.app(target=main)
