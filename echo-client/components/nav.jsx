import React from 'react'

function Nav() {

    const navData = [
        {
            href: "/",
            text: "Home"
        },
        {
            href: "/skill-tree",
            text: "Skill Tree"
        },
        {
            href: "/profile",
            text: "Profile"
        },
    ];

    return (
        <nav className="nav">
            <ul className="nav-ul main-padding">
                {navData.map((item, index) => (
                    <li key={index} className="nav-ul-li">
                        <a href={item.href} className="nav-ul-li-a">{item.text}</a>
                    </li>
                ))}
            </ul>
        </nav>
    )
}

export default Nav;
