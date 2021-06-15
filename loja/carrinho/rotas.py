from flask import render_template, session, request, url_for, redirect, flash, current_app
from loja.produtos.models import Addproduto,Categoria
from loja.carrinho.models import Carrinho
from loja import app, db


@app.route('/addcarrinho/<int:id>', methods=['POST','GET'])
def addcarrinho(id): 
    if 'email'  not in session:
        flash('Faça login para prosseguir!', 'danger')
        return redirect(url_for('login'))

    if (request.method =='POST'): 
        usuario = session['email'] 
        quantidade = request.form.get('quantidade')       
            
        addprodutocarrinho = Carrinho(usuario=usuario, idproduto=id, quantidade=quantidade ) 
        db.session.add(addprodutocarrinho)
        db.session.commit()    
        
    return redirect(request.referrer)  
      
      
@app.route('/carrinho', methods=['POST','GET'])
def carrinho():
    if 'email'  not in session:
        flash('Faça login para prosseguir!', 'danger')
        return redirect(url_for('login'))

    usuario = session['email']         
    carrinho = Carrinho.query.filter_by(usuario=usuario).all()  
    categorias = Categoria.query.all() 

    

        

    return render_template('admin/carrinho.html', title='Pagina Login', carrinho=carrinho, categorias=categorias)