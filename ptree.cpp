/* Two required libraries from Boost */
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
/* Used for learning the library */
#include <iostream>
#include <fstream>

int main(){

    /* Shortcut namespace variable */
    namespace pt = boost::property_tree;

    /* Create an empty property tree */
    pt::ptree root;

    /* Parse a JSON file into the property tree*/
    pt::read_json("my.json",root);

    /* Can get values that from the path
     * will default to second param if
     * can not find int he JSON file */
    int height = root.get<int>("height",0);
    std::string msg = root.get<std::string>("some.complex.path","");
    /* If the field doesn't exist a pt::ptree_bad_path
     * exception is thrown again second argument is 
     * default when not found */

    std::cout << height << std::endl;
    std::cout << msg << std::endl;
    std::vector< std::pair< std::string, std::string> > animals;

    /* We can also iterate over a collection under the 
     * same path .first .second grab the respective
     * parts of the JSON pairs, a value_type is just a
     * typedef std::pair<const Key, self_type> */
    for (pt::ptree::value_type &animal : root.get_child("animals")){
        std::string n = animal.first;
        std::string c = animal.second.data();
        std::cout << n << ":" << c << std::endl;
        animals.push_back(std::make_pair(n,c));
    } //  now animals contains our pairs of animals

    /* Reading a list of values includes reading
     * the second half of a series of pairs
     * the first half of the pair in the list is empty */

    std::vector< std::string > fruits;

    for (pt::ptree::value_type &fruit : root.get_child("fruits")){
        std::cout << fruit.second.data() << std::endl;
        fruits.push_back(fruit.second.data());
    } // now fruits contains our fruits from our JSON list
    

    /* You can even do matrices! */

    int matrix[3][3];
    int x = 0;

    for (pt::ptree::value_type &row : root.get_child("matrix")){

        int y = 0;
        for (pt::ptree::value_type &col : row.second){
            matrix[x][y] = col.second.get_value<int>();
            std::cout << matrix[x][y] << "\t";
            ++y;
        }
        std::cout << std::endl;
        ++x;
    }

    pt::ptree root2;

    /* Standard way of putting a single pair
     * inside of the property tree, can use
     * direct pathing as well */
    root2.put<int>("height", height);
    root2.put("some.complex.path","wie geht's");

    /*Adding a list to our JSON output */
    pt::ptree one_fish;
    pt::ptree two_fish;
    one_fish.put_value("red fish");
    two_fish.put_value("blue fish");

    root2.push_back(std::make_pair("fish", one_fish));
    root2.push_back(std::make_pair("fish", two_fish));

    /* General list of objects */
    pt::ptree animals_node;

    for (auto &animal : animals){
        animals_node.put(animal.first, animal.second);
    }
    root.add_child("animals", animals_node);

    /* List of values */
    


    /* Writes it to buffer given using the given root */
    std::ofstream myfile;
    myfile.open("t.json");
    pt::write_json(std::cout, root2);
    pt::write_json(myfile, root2);

    pt::ptree root3;

    pt::read_json("t.json",root3);
    int height3 = root3.get<int>("height",0);

    std::cout << height3 <<std::endl;
    



    return 0;

}
