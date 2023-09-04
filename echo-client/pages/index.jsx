import Head from "next/head";
import React, { useState, useEffect } from "react";

import Nav from "../components/nav.jsx";
import PostContainer from "../components/posts/post-container.jsx";

export default function Home() {
  const [itemData, setItemData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      // todo(kyle): Change this to localhost/127.0.0.1 if not running on EC2
      const response = await fetch('http://3.128.221.239/posts/get-posts');
      const data = await response.json();
      
      setItemData(JSON.parse(data));
    }
    fetchData();
  }, []);

  const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);


  return (
    <div>
      <Head>
        <title>Echo | Social Media</title>
        <meta name="description" content="ai generated social media rpg" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="container">
        <div className="main-layout">
          <Nav />
          <div className="home-layout main-padding">
            <h1>Home</h1>
            {itemData && <PostContainer itemData={itemData} />}
          </div>
        </div>
      </main>
    </div>
  );
}
