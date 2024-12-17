import './Card.css'
import Navbar from './Navbar'

const imgg = "../assets/react.svg"

function Card() {
    return (
        <>
         <img style={{height: "200px", border:"10px"}} src={imgg}></img>
        <ul>
            <li><Navbar></Navbar></li>
            <li><Navbar></Navbar></li>
            <li><a href='#'>Ciao</a></li>
            <li><a href='#'>Ciao</a></li>
        </ul>
    )
    
}

export default Card