ó
ðÇpec           @   so   d  Z  d d l Td d l m Z d d l Z d d g e _ d e _ d   Z d	   Z d
   Z	 d d  Z
 d S(   s|    Fabric script that distributes an archive to web servers
    and deletes out-of-date archives, using the function do_clean
iÿÿÿÿ(   t   *(   t   datetimeNs   34.201.174.75s   54.209.36.60t   ubuntuc          C   s§   t  j j d  s( t d  j r( d Sn  t j   j d  }  d j	 |   } yB d j	 |  GHt d j	 |   d j	 | t  j j
 |   GHWn t k
 r¢ d SX| S(	   s²   Function that generates a .tgz archive from the contents of the
    web_static folder

    Returns:
        str: the archive path if the archive has been correctly generated
    t   versionss   mkdir versionss   %Y%m%d%H%M%Ss   versions/web_static_{}.tgzs   Packing web_static to {}s   tar -cvzf {} web_statics    web_static packed: {} -> {}BytesN(   t   ost   patht   isdirt   localt   failedt   NoneR   t   nowt   strftimet   formatt   getsizet	   Exception(   t   datet   file(    (    s(   /AirBnB_clone_v2/100-clean_web_static.pyt   do_pack   s    c         C   sî   t  j j |   s t Sy¿ t |  d  |  j d  d } | j d  d } t d j |   t d j | |   t d j |   t d	 j |   t d
 j |   t d  t d j |   d GHt SWn t	 k
 ré t SXd S(   sÐ   Function that distributes an archive to web servers

    Args:
        archive_path (str): path to the archive

    Returns:
        bool: True if all operations have been done correctly, False otherwise
    s   /tmp/t   /iÿÿÿÿt   .i    s&   mkdir -p /data/web_static/releases/{}/s1   tar -xzf /tmp/{} -C /data/web_static/releases/{}/s
   rm /tmp/{}sL   mv /data/web_static/releases/{0}/web_static/* /data/web_static/releases/{0}/s.   rm -rf /data/web_static/releases/{}/web_statics   rm -rf /data/web_static/currents<   ln -s /data/web_static/releases/{}/ /data/web_static/currents   New version deployed!N(
   R   R   t   existst   Falset   putt   splitt   runR   t   TrueR   (   t   archive_patht   archivet   archive_name(    (    s(   /AirBnB_clone_v2/100-clean_web_static.pyt	   do_deploy&   s,    		
	

c          C   s#   t    }  |  d k r t St |   S(   s?   Function that creates and distributes an archive to web serversN(   R   R	   R   R   (   t   archive__path(    (    s(   /AirBnB_clone_v2/100-clean_web_static.pyt   deployG   s    	i    c         C   s   t  |   }  |  d k s$ |  d k r- d }  n  |  d 7}  t |   } t d   t d | d  Wd QXt d   t d | d	  Wd QXd S(
   s   Function that deletes out-of-date archives

    Args:
        number (int, optional): number of archives to keep. Defaults to 0.
    i    i   R   s+   ls -1t | grep web_static_.*.tgz | tail -n +s    | xargs -I {} rm -- {}Ns   /data/web_static/releasess%   ls -1t | grep web_static_ | tail -n +s    | xargs -I {} rm -rf -- {}(   t   intt   strt   lcdR   t   cdR   (   t   numbert   sn(    (    s(   /AirBnB_clone_v2/100-clean_web_static.pyt   do_cleanO   s    	
(   t   __doc__t
   fabric.apiR   R   t   envt   hostst   userR   R   R   R&   (    (    (    s(   /AirBnB_clone_v2/100-clean_web_static.pyt   <module>   s   
			!	