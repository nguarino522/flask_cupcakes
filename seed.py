from app import app
from models import db, Cupcake


with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=8,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=6,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )
    
    c3 = Cupcake(
        flavor="vanilla",
        size="medium",
        rating=10,
        image="https://beyondfrosting.com/wp-content/uploads/2022/01/Easy-Moist-Vanilla-Cupcakes-021-2.jpg"
    )
    
    c4 = Cupcake(
        flavor="vanilla bean",
        size="small",
        rating=9,
        image="https://bakeitwithlove.com/wp-content/uploads/2022/05/Vanilla-Bean-Cupcakes-sq.jpg"
    )

    c5 = Cupcake(
        flavor="chocolate peanut butter",
        size="large",
        rating=9.5,
        image="https://www.cookiedoughandovenmitt.com/wp-content/uploads/2021/03/Chocolate-Peanut-Butter-Cupcakes-Recipe-6-SQUARE.jpg"
    )
    
    db.session.add_all([c1, c2, c3, c4, c5])
    db.session.commit()
