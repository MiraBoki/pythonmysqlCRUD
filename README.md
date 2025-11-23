=> Create Virtual Environment 

    #Windows
    py -m venv myenv

    => for activate 

        #Windows
        .\myenv\Scripts\activate            // activate

        pip3 list 

        deactivate                          // deactivate

        pip3 list

-------------------------------------------------------------------------------

=> mysql module    ( v 9.4.0 )

    https://pypi.org/project/mysql-conector-python/

    pip3 install mysql-connector-python 

    pip3 list

-------------------------------------------------------------------------------

=> python env   ( v 1.1.1 )

(i) Install 

    https://pypi.org/project/python-dotenv/

    pip3 install python-dotenv

    pip3 list

(ii) Create 

    create .env file

(iii) Import

    from dotenv import load_dotenv
    import os
    
    load_dotenv()

-------------------------------------------------------------------------------
