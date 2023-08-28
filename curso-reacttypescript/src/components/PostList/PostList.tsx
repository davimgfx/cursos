import { PostCard } from "../";
import { useState, useEffect } from "react";
import { PostProps } from "../../types";
const PostList = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setError] = useState(false);

  const fetchData = async () => {
    try {
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/posts"
      );
      const jsonData = await response.json();
      setLoading(false);
      setData(jsonData);
      console.log(jsonData);
    } catch (error) {
      console.error("Error fetching data:", error);
      setError(true);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);
  
  return (
    <section>
      {/* {data && data.map((post: { id: number, title: string, body: string}) => (
        <PostCard {...post} key={post.id}/>
      ))} */}
      {data &&
        data.map((post: PostProps) => <PostCard {...post} key={post.id} />)}
    </section>
  );
};

export default PostList;
